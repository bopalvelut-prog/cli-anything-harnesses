import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['php', 'artisan', 'serve'])
@cli.command()
def migrate(): subprocess.run(['php', 'artisan', 'migrate'])
if __name__ == '__main__': cli()
