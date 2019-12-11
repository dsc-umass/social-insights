# health-insights
A big data project on building a public API with insights to a dataset for healthcare


## Getting Started



### Prerequisites

To run and setup the project you need node.js and NPM installed for the visualizations, which can be found [here](https://nodejs.org/en/). For the data processing you need python which can found [here](https://www.python.org/downloads/release/python-374/).

### Installing

To get started on visualizations:
```
git clone https://github.com/dsc-umass/meetsync.git

cd health-insights/visualizations

npm install
```

## Deployment

To get started on visualizations:
```
cd dataproc/

sudo pm2 start api.py --name health-insights --interpreter=python3
```

## Built With

* [GCP Dataproc](https://cloud.google.com/dataproc/) - Spark and Hadoop on the Cloud
* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - API Framework
* [PM2](https://pm2.keymetrics.io/) - Production Server and Load Balancing

<!-- 
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. -->

<!-- 
## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. -->

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
<!-- 
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->


