const vokaNFT = artifacts.require("vokaNFT");

module.exports = function (deployer) {
  deployer.deploy(vokaNFT);
};
