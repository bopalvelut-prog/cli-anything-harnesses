import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oss running')
@cli.command()
def start(): click.echo('oss started')
if __name__ == '__main__': cli()
