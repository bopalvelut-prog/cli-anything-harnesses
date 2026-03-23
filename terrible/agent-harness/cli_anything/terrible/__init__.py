import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('terrible running')
@cli.command()
def start(): click.echo('terrible started')
if __name__ == '__main__': cli()
