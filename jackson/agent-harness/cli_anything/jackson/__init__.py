import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jackson running')
@cli.command()
def start(): click.echo('jackson started')
if __name__ == '__main__': cli()
