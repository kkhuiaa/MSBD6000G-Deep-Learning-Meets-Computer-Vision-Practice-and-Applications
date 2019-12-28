import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################

  train_count = X.shape[0]
  train_class = W.shape[1]
  score = X.dot(W)

  for i in xrange(train_count):
    #Calculate the score accordingly

    #Substract the max for numerical stability (to make all the values negative)
    shifted_s = score[i, :] - np.max(score[i, :])

    #Calculate the loss for this sample data
    loss += np.log(np.sum(np.exp(shifted_s))) - shifted_s[y[i]]

    #Calculate the softmax score here
    for j in range(train_class):
      softmax_s = np.exp(shifted_s[j]) / np.sum(np.exp(shifted_s))

      if j  == y[i]: #equal to the correct label
        dW[:, j] += X[i]*(softmax_s-1)
      else:
        dW[:, j] += X[i]*softmax_s

  #Calculate the loss
  loss = loss/train_count + reg*np.sum(W*W)
  
  #Calculate the dW
  dW = dW/train_count + 2*reg*W

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  train_count = X.shape[0]

  #Calculate the score
  s = X.dot(W)

  #Substract the max for numerical stability (to make all the values negative)
  shifted_s = s - np.max(s, axis=1)[:, np.newaxis]

  #Calculate the softmax score here
  softmax_s = np.exp(shifted_s)/np.sum(np.exp(shifted_s), axis=1)[:, np.newaxis]

  #Calculate the loss for this sample data
  loss = -np.sum(np.log(softmax_s[range(0, train_count), y]))
  loss = loss/train_count + reg*np.sum(W**2)
  
  #Calculate the dW
  softmax_s[range(train_count), y] -=1
  dW = X.T.dot(softmax_s)
  dW = dW/train_count + 2*W*reg

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

