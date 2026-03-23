import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lawn running')
@cli.command()
def start(): click.echo('lawn started')
if __name__ == '__main__': cli()
