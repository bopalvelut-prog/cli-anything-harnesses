import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('coal running')
@cli.command()
def start(): click.echo('coal started')
if __name__ == '__main__': cli()
