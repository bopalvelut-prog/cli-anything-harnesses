import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thirty running')
@cli.command()
def start(): click.echo('thirty started')
if __name__ == '__main__': cli()
