import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deaf running')
@cli.command()
def start(): click.echo('deaf started')
if __name__ == '__main__': cli()
