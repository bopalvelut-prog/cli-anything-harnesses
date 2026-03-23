import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('news running')
@cli.command()
def start(): click.echo('news started')
if __name__ == '__main__': cli()
