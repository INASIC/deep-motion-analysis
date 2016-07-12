from __future__ import print_function

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, TimeDistributed
from keras.layers import LSTM, GRU
from keras.optimizers import Nadam
import keras
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import theano
sys.path.append('../../utils/')
from visualise import visualise

# build the model: 2 stacked LSTM
print('Build model...')
model = Sequential()
model.add(TimeDistributed(Dense(256), input_shape=(29,256)))
model.add(Activation(keras.layers.advanced_activations.ELU(alpha=1.0)))
model.add(GRU(256, return_sequences=True, consume_less='gpu', \
                init='glorot_normal'))
model.add(Dropout(0.117))
model.add(GRU(512, return_sequences=True, consume_less='gpu', \
               init='glorot_normal'))
model.add(Dropout(0.0266))
model.add(TimeDistributed(Dense(256)))
model.add(Activation(keras.layers.advanced_activations.ELU(alpha=1.0)))
# TimedistributedDense on top - Can then set output vectors to be next sequence!

model.compile(loss='mean_squared_error', optimizer='nadam')


visualise(model, '2GRU-0.6.hd5', frame=3, num_frame_pred=1, anim_frame_start=55, anim_frame_end=56)