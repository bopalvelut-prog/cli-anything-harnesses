import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prepare running')
@cli.command()
def start(): click.echo('prepare started')
if __name__ == '__main__': cli()
