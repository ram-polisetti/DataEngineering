# Installation Steps for HashiCorp Terraform

**Step 1:** Ensure that your system is up to date and have installed the required packages:

```shell
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
```

**Step 2:** Install the HashiCorp GPG key:

```shell
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
```

**Step 3:** Verify the key's fingerprint:

```shell
gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint
```

The gpg command will report the key fingerprint, which you should verify.

**Step 4:** Add the official HashiCorp repository to your system:

```shell
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list
```

**Step 5:** Download the package information from HashiCorp:

```shell
sudo apt update
```

**Step 6:** Install Terraform from the new repository:

```shell
sudo apt-get install terraform
```

After following these steps, you can verify the installation by running Terraform commands. For example:

**Verify Terraform installation:**

```shell
terraform -help
```

This will display Terraform's available subcommands. You can use the `-help` flag with any subcommand to learn more about what it does and available options. For example:

**Learn more about the "plan" subcommand:**

```shell
terraform -help plan
```

These steps will help you install and verify Terraform on your system.
