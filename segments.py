from matplotlib.pylab import gca, figure, plot, subplot, title, xlabel, ylabel, xlim,show
import db_queries
from numpy import arange, array, ones
from numpy.linalg import lstsq
from matplotlib.lines import Line2D


def segments(data):

#    data = db_queries.prova()
    max_error = 2
    print(len(data))

    figure()
    segments = slidingwindowsegment(data, regression, sumsquared_error, max_error)
    draw_plot(data,"Sliding window with regression")
    draw_segments(segments)
    show()
    return segments
    #figure()
    #segments = topdownsegment(data,interpolate,sumsquared_error,max_error)
    #print(len(segments))
    #print(segments)
    #draw_plot(data, "Top down with simple interpolation")
    #show()
    #draw_segments(segments)
    #show()


def slidingwindowsegment(sequence, create_segment, compute_error, max_error, seq_range=None):
    """
    Return a list of line segments that approximate the sequence.

    The list is computed using the sliding window technique.

    Parameters
    ----------
    sequence : sequence to segment
    create_segment : a function of two arguments (sequence, sequence range) that returns a line segment that approximates the sequence data in the specified range
    compute_error: a function of two argments (sequence, segment) that returns the error from fitting the specified line segment to the sequence data
    max_error: the maximum allowable line segment fitting error

    """
    if not seq_range:
        seq_range = (0,len(sequence)-1)
    start = seq_range[0]
    end = start
    array = []
    result_segment = create_segment(sequence,(seq_range[0],seq_range[1]))
    while end < seq_range[1]:
        end += 1
        test_segment = create_segment(sequence,(start,end))
        error = compute_error(sequence,test_segment)
        if error <= max_error:
            result_segment = test_segment
        else:
            array.append(result_segment)
            start = end-1

    if end == seq_range[1]:
        array.append(result_segment)
    return array
    #else:
     #   return [result_segment] + slidingwindowsegment(sequence, create_segment, compute_error, max_error, (end-1,seq_range[1]))


def regression(sequence, seq_range):
    """Return (x0,y0,x1,y1) of a line fit to a segment of a sequence using linear regression"""
    p, error = leastsquareslinefit(sequence, seq_range)
    y0 = p[0] * seq_range[0] + p[1]
    y1 = p[0] * seq_range[1] + p[1]
    return (seq_range[0], y0, seq_range[1], y1)

def leastsquareslinefit(sequence,seq_range):
    """Return the parameters and error for a least squares line fit of one segment of a sequence"""
    x = arange(seq_range[0],seq_range[1]+1)
    y = array(sequence[seq_range[0]:seq_range[1]+1])
    A = ones((len(x),2),float)
    A[:,0] = x
    (p,residuals,rank,s) = lstsq(A,y)
    try:
        error = residuals[0]
    except IndexError:
        error = 0.0
    return (p,error)

def sumsquared_error(sequence, segment):
    """Return the sum of squared errors for a least squares line fit of one segment of a sequence"""
    x0,y0,x1,y1 = segment
    p, error = leastsquareslinefit(sequence,(x0,x1))
    return error


def topdownsegment(sequence, create_segment, compute_error, max_error, seq_range=None):
    """
    Return a list of line segments that approximate the sequence.

    The list is computed using the bottom-up technique.

    Parameters
    ----------
    sequence : sequence to segment
    create_segment : a function of two arguments (sequence, sequence range) that returns a line segment that approximates the sequence data in the specified range
    compute_error: a function of two argments (sequence, segment) that returns the error from fitting the specified line segment to the sequence data
    max_error: the maximum allowable line segment fitting error

    """
    if not seq_range:
        seq_range = (0, len(sequence) - 1)

    bestlefterror, bestleftsegment = float('inf'), None
    bestrighterror, bestrightsegment = float('inf'), None
    bestidx = None

    for idx in range(seq_range[0] + 1, seq_range[1]):
        segment_left = create_segment(sequence, (seq_range[0], idx))
        error_left = compute_error(sequence, segment_left)
        segment_right = create_segment(sequence, (idx, seq_range[1]))
        error_right = compute_error(sequence, segment_right)
        if error_left + error_right < bestlefterror + bestrighterror:
            bestlefterror, bestrighterror = error_left, error_right
            bestleftsegment, bestrightsegment = segment_left, segment_right
            bestidx = idx

    if bestlefterror <= max_error:
        leftsegs = [bestleftsegment]
    else:
        leftsegs = topdownsegment(sequence, create_segment, compute_error, max_error, (seq_range[0], bestidx))

    if bestrighterror <= max_error:
        rightsegs = [bestrightsegment]
    else:
        rightsegs = topdownsegment(sequence, create_segment, compute_error, max_error, (bestidx, seq_range[1]))

    return leftsegs + rightsegs

def interpolate(sequence, seq_range):
    """Return (x0,y0,x1,y1) of a line fit to a segment using a simple interpolation"""
    return (seq_range[0], sequence[seq_range[0]], seq_range[1], sequence[seq_range[1]])

def draw_plot(data,plot_title):
    plot(range(len(data)),data,alpha=0.8,color='blue')
    title(plot_title)
    xlabel("Samples")
    ylabel("Signal")
    xlim((0,len(data)-1))

def draw_segments(segments):
    ax = gca()
   # fig=figure()
    #ax = fig.add_subplot(111)

    for segment in segments:
        line = Line2D((segment[0],segment[2]),(segment[1],segment[3]))
        ax.add_line(line)
    #ax.plot()
    #fig.show()

