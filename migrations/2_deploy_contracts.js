const vokaNFT = artifacts.require("vokaNFT");
const myCounter = artifacts.require("myCounter");

module.exports = function (deployer) {
  deployer.deploy(vokaNFT);
  deployer.deploy(myCounter);
};
