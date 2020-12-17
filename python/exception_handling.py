{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.5\n"
     ]
    }
   ],
   "source": [
    "#This one will not throw us any error\n",
    "a = 5\n",
    "b = 2\n",
    "\n",
    "print(a/b)\n",
    "\n",
    "# Output\n",
    "# 2.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-ae35ad0b8fa2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m/\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;31m# Output\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#By avoid giving error instead we use try, except, finally method to avoid interruption\n",
    "a = 5\n",
    "b = 0\n",
    "\n",
    "print(a/b ) \n",
    "\n",
    "# Output\n",
    "# ZeroDivisionError                         Traceback (most recent call last)\n",
    "# <ipython-input-2-5e50c599d0aa> in <module>\n",
    "#       2 b = 0\n",
    "#       3 \n",
    "# ----> 4 print(a/b)\n",
    "\n",
    "# ZeroDivisionError: division by zero"
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
      "***Resource open***\n",
      "\n",
      " 2.5\n",
      "The above result of a/b printed sucessfully\n",
      "Enter the value:p\n",
      "\n",
      "***Invalid Input***\n",
      "\n",
      "***Resource closed***\n"
     ]
    }
   ],
   "source": [
    "a = 5\n",
    "b = 2\n",
    "\n",
    "try:\n",
    "    print(\"***Resource open***\")\n",
    "    print(\"\\n\",a/b)\n",
    "\n",
    "except ZeroDivisionError as e:\n",
    "    print(\"We cannot divide number by zero\", e)\n",
    "finally:\n",
    "    print(\"The above result of a/b printed sucessfully\")\n",
    "\n",
    "try:\n",
    "    x = int(input(\"Enter the value:\"))\n",
    "    print(x)\n",
    "\n",
    "except ValueError as e:\n",
    "    print(\"\\n***Invalid Input***\")\n",
    "    \n",
    "finally:\n",
    "    print(\"\\n***Resource closed***\")\n",
    "    \n",
    "# Output\n",
    "\n",
    "# ***Resource open***\n",
    "\n",
    "#  2.5\n",
    "# The above result of a/b printed sucessfully\n",
    "# Enter the value:p\n",
    "\n",
    "# ***Invalid Input***\n",
    "\n",
    "# ***Resource closed***"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
