import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('LM Studio start')
@cli.command()
def models(): click.echo('LM Studio models')
if __name__ == '__main__': cli()
