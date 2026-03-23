import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('honest running')
@cli.command()
def start(): click.echo('honest started')
if __name__ == '__main__': cli()
