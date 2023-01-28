# MongoDB Exercise

This repository contains my solutions for a MongoDB exercise. The exercise is focused on manipulating a dataset of restaurants using MongoDB's query language and the PyMongo library. The dataset is provided in the `data` folder. The solutions are provided in the `solutions` folder, each solution is in separate python file `solutionx.py`

## Getting Started

1.  Make sure you have MongoDB installed and running on your machine.
2.  Clone this repository and navigate to the root directory.
3.  Make sure you have MongoDB and PyMongo installed.
4.  Create a `.env` file in the `solutions/config` folder and add the MongoDB connection string as a variable `MONGO_HOST`, username as `MONGO_USERNAME` and password as `MONGO_PASSWORD`
4.  Import the `restaurants.json` file to your MongoDB by running the following command:

```BASH
mongoimport --db restaurants --collection addresses --file data/restaurants.json
```


## Questions

For the questions , check the `questions.md` file in the root directory.

## Credits

- Thanks to  [@KasunDissanayake94](https://github.com/KasunDissanayake94) for providing the MongoDB exercise and the dataset .
