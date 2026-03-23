import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xpl running')
@cli.command()
def start(): click.echo('xpl started')
if __name__ == '__main__': cli()
