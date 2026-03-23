import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('predict running')
@cli.command()
def start(): click.echo('predict started')
if __name__ == '__main__': cli()
