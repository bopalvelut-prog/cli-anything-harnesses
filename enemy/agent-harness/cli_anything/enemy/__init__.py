import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('enemy running')
@cli.command()
def start(): click.echo('enemy started')
if __name__ == '__main__': cli()
