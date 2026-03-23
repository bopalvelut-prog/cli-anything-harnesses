import click
@click.group()
def cli(): pass
@cli.command()
def search(): click.echo('Perplexity search')
@cli.command()
def models(): click.echo('Perplexity models')
if __name__ == '__main__': cli()
