import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('script')
def run(script): subprocess.run(['ruby', script])
@cli.command()
def install(): subprocess.run(['bundle', 'install'])
@cli.command()
def test(): subprocess.run(['ruby', '-Ilib', '-e', "require 'minitest/autorun'; Dir.glob('test/**/*.rb').each{|f| require './#{f}'}"])
if __name__ == '__main__': cli()
