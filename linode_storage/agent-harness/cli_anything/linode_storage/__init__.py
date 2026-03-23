import click
@click.group()
def cli(): pass
@cli.command()
def buckets(): click.echo('Storage buckets')
@cli.command()
def objects(): click.echo('Storage objects')
if __name__ == '__main__': cli()
