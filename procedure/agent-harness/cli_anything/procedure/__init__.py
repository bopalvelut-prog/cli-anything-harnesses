import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('procedure running')
@cli.command()
def start(): click.echo('procedure started')
if __name__ == '__main__': cli()
