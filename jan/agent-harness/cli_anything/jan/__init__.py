import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Jan start')
@cli.command()
def models(): click.echo('Jan models')
if __name__ == '__main__': cli()
