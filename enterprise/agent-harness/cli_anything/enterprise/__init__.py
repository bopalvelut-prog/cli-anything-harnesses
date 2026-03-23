import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('enterprise running')
@cli.command()
def start(): click.echo('enterprise started')
if __name__ == '__main__': cli()
