import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dredd running')
@cli.command()
def start(): click.echo('dredd started')
if __name__ == '__main__': cli()
