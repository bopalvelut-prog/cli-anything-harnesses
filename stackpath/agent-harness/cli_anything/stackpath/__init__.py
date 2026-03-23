import click
@click.group()
def cli(): pass
@cli.command()
def purge(): click.echo('StackPath purge')
@cli.command()
def sites(): click.echo('StackPath sites')
if __name__ == '__main__': cli()
