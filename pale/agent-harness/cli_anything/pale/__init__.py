import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pale running')
@cli.command()
def start(): click.echo('pale started')
if __name__ == '__main__': cli()
