{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " pytesseract library install करा "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pytesseract"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from PIL import Image     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyttsx3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For english english lang image path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = r\"C:\\Users\\Siddesh\\Desktop\\OCR\\study\\file.png\"\n",
    "file = Image.open(img)"
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
      "<PIL.PngImagePlugin.PngImageFile image mode=P size=658x402 at 0x364D126EC8>\n"
     ]
    }
   ],
   "source": [
    "print(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "result = pytesseract.image_to_string(file)    "
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
      "Hey [Endearment],\n",
      "I'm standing staring at my surroundings, but my mind keeps\n",
      "drifting back you to and how good we are together. | can still taste the sweetness of\n",
      "your lips against mine; the feel of your skin as | slide my fingers along your silky\n",
      "\n",
      "smoothness.\n",
      "\n",
      "It's the simple things about you that turn me inside out; but, when we kiss, | burn raw.\n",
      "deep down inside. | crave that next kiss; the one that always leads to more.\n",
      "\n",
      "Until our next kiss.\n",
      "\n",
      "x0x0x0x0x0x0\n"
     ]
    }
   ],
   "source": [
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "for marathi language image path "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "txt = r\"C:\\Users\\Siddesh\\Desktop\\OCR\\study\\1.jpg\"\n",
    "text = Image.open(txt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "result = pytesseract.image_to_string(text,lang ='mar')   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "लेखांपर्यंत पोहचण्याचे इतर मार्ग [संपादन]\n",
      "*« विकिपीडिया कॅटेगरी हा लेखांपर्यंत पोहचण्याकरिता उपलब्ध अनेक मार्गांपैकी एक मार्ग झाला.विस्तृत माहिती करिता विकिपीडिया:सफर हा लेख वाचा\n",
      "« * विकिपीडिया परस्पर सांधणी,\n",
      "* विकिपीडिया शोधयंत्र,\n",
      "*« विकिपीडिया वर्णमाला आधारित अनुक्रमणिका,\n",
      "*« विकिपीडिया येथे काय जोडले आहे\n",
      "* विकिपीडिया दालन,\n",
      "*« विकिपीडिया प्रकल्प,\n",
      "* दिदोष पृष्ठ\n",
      "*« अविशिष्ट लेख,\n",
      "* अलीकडील बदल,\n",
      "* सदस्याचे योगदान,\n",
      "* सारणी,\n",
      "* साचे,\n",
      "* लेखांची यादी\n",
      "* आंतरभाषा विकीदुवा-जोड\n",
      "* गूगल इत्यादी शोधयंत्राने दिलेले शोध\n",
      "* इतर संकेतस्थळांनी दिलेले दुवे इत्यादी पर्याय उपलब्ध आहेत.\n"
     ]
    }
   ],
   "source": [
    "print(result)"
   ]
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
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

