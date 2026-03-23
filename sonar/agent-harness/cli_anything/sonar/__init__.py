import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sonar running')
@cli.command()
def start(): click.echo('sonar started')
if __name__ == '__main__': cli()
