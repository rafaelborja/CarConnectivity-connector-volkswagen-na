# CarConnectivity Connector for Volkswagen North American Vehicles

[![GitHub sourcecode](https://img.shields.io/badge/Source-GitHub-green)](https://github.com/zackcornelius/CarConnectivity-connector-volkswagen-na/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/zackcornelius/CarConnectivity-connector-volkswagen-na)](https://github.com/zackcornelius/CarConnectivity-connector-volkswagen-na/releases/latest)
[![GitHub](https://img.shields.io/github/license/zackcornelius/CarConnectivity-connector-volkswagen-na)](https://github.com/zackcornelius/CarConnectivity-connector-volkswagen-na/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/zackcornelius/CarConnectivity-connector-volkswagen-na)](https://github.com/zackcornelius/CarConnectivity-connector-volkswagen-na/issues)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/carconnectivity-connector-volkswagen-na?label=PyPI%20Downloads)](https://pypi.org/project/carconnectivity-connector-volkswagen-na/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/carconnectivity-connector-volkswagen-na)](https://pypi.org/project/carconnectivity-connector-volkswagen-na/)
[![Donate at PayPal](https://img.shields.io/badge/Donate-PayPal-2997d8)](https://www.paypal.com/donate?hosted_button_id=2BVFF5GJ9SXAJ)
[![Sponsor at Github](https://img.shields.io/badge/Sponsor-GitHub-28a745)](https://github.com/sponsors/tillsteinbach)

## CarConnectivity will become the successor of [WeConnect-python](https://github.com/tillsteinbach/WeConnect-python) in 2025 with similar functionality but support for other brands beyond Volkswagen!

[CarConnectivity](https://github.com/tillsteinbach/CarConnectivity) is a python API to connect to various car services. This connector enables the integration of volkswagen vehicles through the WeConnect API. Look at [CarConnectivity](https://github.com/tillsteinbach/CarConnectivity) for other supported brands.

## Configuration

In your carconnectivity.json configuration add a section for the volkswagen connector like this:

```json
{
  "carConnectivity": {
    "connectors": [
      {
        "type": "volkswagen_na",
        "config": {
          "username": "test@test.de",
          "password": "testpassword123",
          "country": "us"
        }
      }
    ]
  }
}
```

Country is optional, and defaults to 'us'. 'ca' may work, but is currently untested.

### Credentials

If you do not want to provide your username or password inside the configuration you have to create a ".netrc" file at the appropriate location (usually this is your home folder):

```
# For MyVW
machine volkswagen_na
login test@test.de
password testpassword123
```

In this case the configuration needs to look like this:

```json
{
  "carConnectivity": {
    "connectors": [
      {
        "type": "volkswagen_na",
        "config": {}
      }
    ]
  }
}
```

You can also provide the location of the netrc file in the configuration.

```json
{
  "carConnectivity": {
    "connectors": [
      {
        "type": "volkswagen_na",
        "config": {
          "netrc": "/some/path/on/your/filesystem"
        }
      }
    ]
  }
}
```

The optional S-PIN needed for some commands can be provided in the account section of the netrc:

```
# For WeConnect
machine volkswagen_na
login test@test.de
password testpassword123
account 1234
```

### Limitations

The connector is tested for US and CA based vehicles, and has the most support for EVs, but does support most (non-remote start) functionality for ICE vehicles as well.

