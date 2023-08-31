<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Music Generation</h3>

  <p align="center">
    Implementation of LSTM neural network to generate piano notes.
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][schema-lstm]


I set up a neural network with 3 LSTM layers (diagram of an LSTM cell above). This network learns from a sequence of 100 notes to generate the next most likely note based on the musical style of the dataset thanks to a machine learning algorithm.

The dataset is made up of a MIDI file, which makes it much easier to manipulate the music file.

The result on [SoundCloud](https://soundcloud.com/gabriel-guiet-dupre-635410161/sets/ai-piano-generation)


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [Python](https://www.python.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [Music21](https://web.mit.edu/music21/doc/)


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage


To get started: 

    pip install tqdm music21 pickle tensorflow

To generate:

    python src/generator.py

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Gabriel GUIET-DUPRE - [in: gabriel-guiet-dupre](https://linkedin.com/in/gabriel-guiet-dupre) - gabriel.guietdupre@edu.ece.fr

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/gabriel-guiet-dupre
[schema-lstm]: ./shema-lstm.png
