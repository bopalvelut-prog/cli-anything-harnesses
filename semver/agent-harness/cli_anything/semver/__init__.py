import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('semver running')
@cli.command()
def start(): click.echo('semver started')
if __name__ == '__main__': cli()
