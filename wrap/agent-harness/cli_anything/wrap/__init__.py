import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wrap running')
@cli.command()
def start(): click.echo('wrap started')
if __name__ == '__main__': cli()
