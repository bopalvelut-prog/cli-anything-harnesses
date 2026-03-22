import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['semgrep', 'scan', '.'])
@cli.command()
def ci(): subprocess.run(['semgrep', 'ci'])
if __name__ == '__main__': cli()
