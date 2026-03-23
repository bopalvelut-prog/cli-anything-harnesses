import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('encounter running')
@cli.command()
def start(): click.echo('encounter started')
if __name__ == '__main__': cli()
