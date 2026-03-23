import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crack running')
@cli.command()
def start(): click.echo('crack started')
if __name__ == '__main__': cli()
