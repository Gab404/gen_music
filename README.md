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

J'ai mis en place un résaux de neuronne avec 3 couches LSTM (shéma d'une cellule LSTM ci-dessus). Ce résau apprend à partir d'une séquence de 100 notes à générer la prochaine note la plus probable en fonction du style musical du dataset.

Le dataset est constitué de fichier MIDI, ce qui permet de manipuler le fichier musical beaucoup plus simplement.


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

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Gabriel GUIET-DUPRE - [in: gabriel-guiet-dupre](https://linkedin.com/in/gabriel-guiet-dupre) - gabriel.guietdupre@edu.ece.fr

Project Link: [https://github.com/gab_gdp/rayCastingVideoGame](https://github.com/Gab404/my_perceptron)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://linkedin.com/in/gabriel-guiet-dupre
[schema-lstm]: ./shema-lstm.png
