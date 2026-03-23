import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('interpret running')
@cli.command()
def start(): click.echo('interpret started')
if __name__ == '__main__': cli()
