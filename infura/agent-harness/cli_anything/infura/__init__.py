import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def endpoints(): click.echo('Infura endpoints')
if __name__ == '__main__': cli()
