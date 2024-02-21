# AWS Connection Script

This Bash script facilitates connecting to an AWS account from a Mac by providing instructions for installing and configuring the AWS Command Line Interface (CLI), including AWS Single Sign-On (SSO) configuration.

## Prerequisites

- MacOS, Linux distro
- Bash shell
- Internet connection
- Homebrew (Mac only)

Before running the script, ensure you have the following tools installed:
- **AWS CLI**: This script relies on the AWS CLI to interact with AWS services. You can install it by running:
    ```bash
    brew install awscli
    ```

- **AWS CLI v2 (optional)**: If you prefer to use AWS CLI version 2, you can install it by running:
    ```bash
    brew install awscli@2
    ```

## Usage

1. Clone or download the script to your local machine.
2. Open a terminal window.
3. Navigate to the directory where the script is located.
4. Run the script with the following command to ensure environment variables are set in the parent shell:
    ```
    source connect-aws.bash
    ```

## Instructions

Follow the prompts provided by the script to install and configure the AWS CLI, including AWS SSO configuration if applicable. Ensure you have your AWS access credentials and default region ready for configuration.

## Feedback

Your feedback is valuable! If you encounter any issues or have suggestions for improvement, please open an issue or reach out to [ronh@comm-it.com](ronh@comm-it.com).

## Resources

- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [Homebrew](https://brew.sh/)

## License

