import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('establish running')
@cli.command()
def start(): click.echo('establish started')
if __name__ == '__main__': cli()
