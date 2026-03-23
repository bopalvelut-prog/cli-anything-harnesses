import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dust running')
@cli.command()
def start(): click.echo('dust started')
if __name__ == '__main__': cli()
