{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "u=\"Hello World\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(u)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "print(u.lower())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO WORLD\n"
     ]
    }
   ],
   "source": [
    "print(u.upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "print(u.capitalize())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "print(len(u))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-7-380efbeef1c2>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-7-380efbeef1c2>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    print(u[0}])\u001b[0m\n\u001b[0m             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "print(u[0}])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "H\n"
     ]
    }
   ],
   "source": [
    "print(u[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "World\n"
     ]
    }
   ],
   "source": [
    "print(u[6:11])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Worl\n"
     ]
    }
   ],
   "source": [
    "print(u[6:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "s=\"HArsh\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "b=\"VArdham\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HArshVArdham\n"
     ]
    }
   ],
   "source": [
    "print(s+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'a' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-14-dfb44bafe443>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m\"\"\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'a' is not defined"
     ]
    }
   ],
   "source": [
    "print(a+\"\"+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HArsh VArdham\n"
     ]
    }
   ],
   "source": [
    "print(s+\" \"+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "s,b=b,s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VArdham\n"
     ]
    }
   ],
   "source": [
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HArsh\n"
     ]
    }
   ],
   "source": [
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdham\n"
     ]
    }
   ],
   "source": [
    "print(s*99)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamVArdhamHArshHArshHArsh\n"
     ]
    }
   ],
   "source": [
    "print(s*99+b*3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print('H' in s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print('h' in s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
