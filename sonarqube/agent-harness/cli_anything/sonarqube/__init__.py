import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): subprocess.run(['sonar-scanner'])
@cli.command()
def status(): click.echo('SonarQube running')
if __name__ == '__main__': cli()
