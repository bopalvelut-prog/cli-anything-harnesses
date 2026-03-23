import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gocd running')
@cli.command()
def start(): click.echo('gocd started')
if __name__ == '__main__': cli()
