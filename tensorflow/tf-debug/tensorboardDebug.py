# just to demo how to startup tensorboard debugger
import numpy as np
import tensorflow as tf
from keras.layers import Input, Dense
from keras.models import Model
# Just disables the warning, doesn't enable AVX/FMA
import os;os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import keras.backend as K
from tensorflow.python import debug as tf_debug
K.set_session(tf_debug.TensorBoardDebugWrapperSession(tf.Session(), "localhost:6007"))

net_in = Input(shape=(3,))
net_out = Dense(1)(net_in)
model = Model(net_in, net_out)
model.compile(loss='mse', optimizer='sgd' )

for batch_no in range(3):
    X_train, Y_train = np.random.rand(32, 3), np.random.rand(32, 1)
    logs = model.train_on_batch(X_train, Y_train)
    print('train loss',logs)

    if batch_no % 1 == 0:
        X_val, Y_val = np.random.rand(32, 3), np.random.rand(32, 1)
        logs = model.evaluate(X_val, Y_val)
        print('valid loss',logs)
#then startup tensorboard server
#tensorboard --logdir=anyFolder --debugger_port 6007
