
<img width="1164" alt="PokemonGen Banner" src="https://github.com/luisdavidgarcia/PokeGenerator/assets/87344382/76034302-ead7-4965-a5f5-87219abae757">

# PokeGenerator: Variational Autoencoder and Latent Diffusion for Sprite Generation

This deep learning project, developed as part of CSC 587 Final Project for Winter 2024, focused on generating Pokémon sprites through advanced machine learning techniques. Our team constructed a variational autoencoder and a latent diffusion reverse multilayer perceptron (MLP) model to innovate in the field of generative models.

## Project Members

<img width="100" height="100" src="./docs/picablu.png" alt="Picablu" align="right">

- Braedan Kennedy (bkenne07@calpoly.edu)
- Luis David Garcia (lgarc120@calpoly.edu)
- Paul Jarski (pjarski@calpoly.edu)
- Briana Kuo (brkuo@calpoly.edu)

## Project Overview

Utilizing a rich dataset of Pokémon sprites, our goal was to generate original sprites that could contribute to extending open-source software such as Pokémon Showdown. The project encompassed dataset preprocessing, model implementation, and an evaluation phase that brought new insights into image generation challenges. A key feature of our project is the use of 512-dimensional latent vectors, offering a robust compressed representation of the original sprites.

## Contents

- `Variational Autoencoder Model`: Our VAE model is symmetrically designed with convolutional layers for encoding and decoding the Pokémon sprites with high fidelity.
- `Latent Diffusion Model`: Following the VAE, this model generates new character sprites by manipulating the latent space.
- `Evaluation Results`: Includes generated images and an interpolation of the VAE's embedding space.
- `Conclusions and Future Work`: Provides insights into future enhancements and practical applications of our model.
- `Report.pdf`: A comprehensive report detailing our methodology, findings, and future directions.
- `Presentation.pdf`: A presentation overviewing the project highlights and visualizations.

## Repository Structure

- `src/`: Source code for the variational autoencoder and latent diffusion model.
- `data/`: Preprocessed dataset used for training the models.
- `models/`: Trained model weights and architecture details.
- `results/`: Generated images and model performance metrics.
- `docs/`: Additional documentation and project report.

## Installation

``` bash
./setup.sh
```

## Environment Activation

``` bash
source venv/bin/activate
```

## Dataset Creation

`cd dataset` and see `README.md`

## Training Model

`cd model` and see `README.md`

## Acknowledgements

We express our gratitude to Professor Jonathan Ventura for his invaluable guidance and support throughout this project.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

---

The PokeGenerator is an embodiment of collaboration and innovation, seeking to push the boundaries of deep learning and generative modeling.

