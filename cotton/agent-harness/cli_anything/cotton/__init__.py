import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cotton running')
@cli.command()
def start(): click.echo('cotton started')
if __name__ == '__main__': cli()
